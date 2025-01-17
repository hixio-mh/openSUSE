#!/bin/bash

set -xEeuo pipefail

ROOK_REPO="github.com/rook/rook"
ROOK_REV="v1.3.4"

if ! command -V go;
then
    echo "ERROR: could not find go binary"
    exit 1
fi

if ! command -V dep;
then
    echo "ERROR: could not find dep binary"
    exit 1
fi

if ! command -V git;
then
    echo "ERROR: could not find git binary"
    exit 1
fi

WORK_DIR=$(mktemp -d -t)
function clean_up {
    echo "cleaning up..."
    chmod -R +w $WORK_DIR
    rm -rf $WORK_DIR
}
trap clean_up EXIT SIGINT SIGTERM

PKG_DIR=$(pwd)
function on_err {
    code="$?"
    set +Eeuo pipefail
    echo "ERROR: previous command has failed"
    echo "Removing archives."
    rm -f $PKG_DIR/rook-$VERSION.tar.xz
    rm -f $PKG_DIR/rook-$VERSION-vendor.tar.xz
    exit $code
}
trap on_err ERR

cat <<EOF

tar-ing Rook $ROOK_REPO at revision '$ROOK_REV'

EOF

GOPATH=$WORK_DIR
GOPATH_ROOK="$GOPATH/src/github.com/rook/rook"

# For dep to get dependencies correctly, git repos must be located in their upstream locations in
# the GOPATH. i.e., we have to clone SUSE/rook to github.com/rook/rook
mkdir --parents $GOPATH_ROOK
git -C $GOPATH_ROOK/.. clone https://$ROOK_REPO.git

cd "$GOPATH_ROOK"
git fetch && git fetch --tags
git checkout "$ROOK_REV"

# e.g, DESCRIBE=v1.1.0-0-g56789def  OR  DESCRIBE=v1.1.0-beta.1-0-g12345abc
describe="$(git describe --long --tags)"
GIT_COMMIT=${describe##*-}       # git commit hash is last hyphen-delimited field
remainder=${describe%-*}         # strip off the git commit field & continue
GIT_COMMIT_NUM=${remainder##*-}  # num of commits after tag is second-to-last hyphen-delimited field
RELEASE=${remainder%-*}          # all content before git commit num is the release version tag
RELEASE=${RELEASE//-/'~'}        # support upstream beta tags: replace hyphen with tilde
RELEASE=${RELEASE:1}             # remove preceding 'v' from beginning of release

# strip off preceding 'v' from RELEASE
VERSION="${RELEASE}+git$GIT_COMMIT_NUM.$GIT_COMMIT"

# make primary source tarball before changing anything in the repo
cd $PKG_DIR
tar -C "$GOPATH_ROOK/.." -cJf rook-$VERSION.tar.xz rook/

# make vendor tarball
cd "$GOPATH_ROOK"

echo "Getting dependencies...might take a while"
GOPATH=$WORK_DIR make mod.check

cd $PKG_DIR
tar -C "$WORK_DIR" -cJf rook-$VERSION-vendor.tar.xz pkg


# update spec file versions
sed -i "s/^Version:.*/Version:        $VERSION/" rook.spec
sed -i "s/^%global rook_container_version .*/%global rook_container_version ${RELEASE}.$GIT_COMMIT_NUM  # this is updated by update-tarball.sh/" rook.spec

echo "Finished successfully!"
