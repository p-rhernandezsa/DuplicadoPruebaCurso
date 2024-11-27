#!/bin/bash
# Encrypts  password in wls environmet   12c
# Set environment.

export MW_HOME=/u01/oracle/fmw/osb12214/product
export WLS_HOME=$MW_HOME/wlserver
export WL_HOME=$WLS_HOME
export JAVA_HOME=/u01/oracle/fmw/osb12214/jdk
export PATH=$JAVA_HOME/bin:$PATH
export DOMAIN_HOME=/u01/oracle/admin/domains/jeedev_prime_domain

. $DOMAIN_HOME/bin/setDomainEnv.sh
java -Dweblogic.security.SSL.ignoreHostnameVerification=true -Dweblogic.security.TrustKeyStore=DemoTrust weblogic.WLST /u01/oracle/admin/domains/jeedev_prime_domain/bin/script-de-instalacion_TPTBK.py -p /u01/oracle/admin/domains/jeedev_prime_domain/bin/config_TPT-dsBK.properties

