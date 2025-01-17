#!/bin/bash

# To check the signature run:
#   echo | gpg
#   gpg --auto-key-locate keyserver --keyserver-options auto-key-retrieve parallel-20200522.tar.bz2.sig

echo | gpg 2>/dev/null
gpg --auto-key-locate keyserver --keyserver-options auto-key-retrieve $0
exit $?

-----BEGIN PGP SIGNATURE-----

iQUHBAABCgAdFiEEzaAaQgjE90UGEH570atFFoiIiIgFAl7JbI0ACgkQ0atFFoiI
iIgx/yagx60zqVyc6TKNteaZ+vU3aIL5yB6kpxwzxy0QrA2RBV9/v2f1fjroorda
w33MIFEXkqKhpVM07jTlsZy05ZK/llI1lUKmyh1jB9qVncZNl5vwZuemZfDigscO
xFwc+5NdI1MQpE64xYoc0g1eFH0ZJzZ3GYjLTRJ1Sn6L0WNUUXXMl+qoy67MRFAS
NFPZ1uCEhdW3T6d5bJdb5c5tK+u6yf0OFKTfAwcFf8BdTBfC2lIx69pWPsedv+XS
naojvnqC3PkTn3Gt/O3/eL36i6yBd+AytVpJBxFDdBWa1t9SzcrokfXvJFj1YcLu
o+U271in5wCX4jblEpkVRRLzVs97UfIMM2QYVpQljTC0iXyDxgb/6eqo9IDP6NRp
AIGStCyy26Ttps73PbtrtKBeSZww1HbrAfZxn/o6zzuRLNwHWApC40JUrYxvhBv1
JNLa2kSvcLeQ5Yey4RO4/qdeV/bhiLOJZB0/0gVb6Q7vjW7PzYKeLEVwfzJ4kljY
jG8kTSHeKXfCq63ouuZEKE5oeE3GDg/pmq0G32PUNIHezcPF3gk0A5lyy6UOHHRV
V5Y+bFir0BCC+BFHobFaIfSIj6Ov8YK5fsC/C4YsZsv6MKzsPhOKNyTWlT6z/CQz
l8MgHFAFB9f1b5qWeD5e+c/xWXsyKSYorRswY42kFx3cYf0vwKX1t4aPFXEueKVs
rqkKVxX/IbDMYN89BT7ONYpglPLKqWr136JeHiTE1Zk+uCv9car4HjDdgT+VZ0Aa
bMtHOcY1n4Q8JBVzq31PZ2nRWHZXlSJOfzGLvGtfweueg6TZbXPaPhirwtpgE0Eo
zKWFP4JYbYPLVRZVfWntFU5O+mvb683rABs1k6ZGrKkyiNkOmjRd3KJk2Gl9xvgp
YekWEqh8RlORSMn6M9QyfZGLGuL/ND7zp256qWSXVOObjQuh3rG4f3yYYlaKgQbA
INaQ7Cj8ahZoCDWfR+7r5ZmubCz0udZA8jFKO1Mbik8YL3id0ItPvavOn7o9002K
axKtb7arY1P++rEElQ10j5ODwVnhPGx7G952bUzdusf9c0p5evzcnJaEAQNsnvFL
ZwKwg26LEwjw0YOJ57ZXzT1kUrdPQNC/Gj9XsuSOEc97GBl2d6SNQ145mtYjVaho
80BU2mzYmPPi1xZaZB5JNpOkRhu5PoZRl0Sxpx+8Bmu/aaINspR5rhdxDXoi+H0O
92DllIWmLofqGkg9RK9/8h+WEDZoyr6Y4xXeilm8Xa27Y1mwqwuDnyvrf2D2I0PY
Qo/umAjNjYRdiJgRxfE+Fcuo6ubpaqwEF/YZj7pSEurjXPsUVQGN+TC1XEgq/fih
EFkSCk0+v6W1NBOZioGPMet0jfeuvYcBYawq3H5SZ+2OPzAbSS3Ve1ixqDB7Pzpo
N87sV8JPJyoWpvT68gGTqoef0TVk/Q1gHDTjLSbkC3Ra5XyuG53zS8dQZZUEPLkW
41VXO1Pr+1KUgMNjmLhVNhCUKD8rHuQSomeaKXFAYW2oi1krR6U0W+V7sI02XUwK
RmODYG2K1nmkMUNEkmUCZhXjRJRWBZyPI1Vcv8JDK/xvXMvrTvMSWpe+HFDbc0ES
tfVlnrrzY0pb0PRP/1mn4YluvBnTFJuTgzFNknl1GdMq6TFR+tyuypPh
=qcHS
-----END PGP SIGNATURE-----
