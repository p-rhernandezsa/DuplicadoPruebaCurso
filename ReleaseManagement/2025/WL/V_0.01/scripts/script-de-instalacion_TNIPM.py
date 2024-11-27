import wlstModule
import time
import getopt
import sys
import re

# Get location of the properties file.
properties = ''
try:
   opts, args = getopt.getopt(sys.argv[1:],"p:h::",["properies="])
except getopt.GetoptError:
   print 'set_datasource.py -p <path-to-properties-file>'
   sys.exit(2)
for opt, arg in opts:
   if opt == '-h':
      print 'set_datasource.py -p <path-to-properties-file>'
      sys.exit()
   elif opt in ("-p", "--properties"):
      properties = arg
print 'properties=', properties

# Load the properties from the properties file.

from java.io import FileInputStream 

propInputStream = FileInputStream(properties)
configProps = Properties()
configProps.load(propInputStream)

# Set all variables from values in properties file.
adminUsername=configProps.get("admin.username")
adminPassword=configProps.get("admin.password")
adminURL=configProps.get("admin.url")
dsPassword=configProps.get("ds.passwordtnipm_user")
dsURL=configProps.get("ds.url")

# Display the variable values.
print 'adminUsername=', adminUsername
print 'adminURL=', adminURL

# Connect to the AdminServer.

connect(adminUsername, adminPassword, adminURL)

print ''
print '======================================================'
print 'The script has been send connect to server'
print '======================================================'
print ''

edit()
startEdit()

cd('/')
cmo.createJDBCSystemResource('jdbc.TNIP')

cd('/JDBCSystemResources/jdbc.TNIP/JDBCResource/jdbc.TNIP')
cmo.setName('jdbc.TNIP')

cd('/JDBCSystemResources/jdbc.TNIP/JDBCResource/jdbc.TNIP/JDBCDataSourceParams/jdbc.TNIP')
set('JNDINames',jarray.array([String('jdbc.TNIP')], String))

cd('/JDBCSystemResources/jdbc.TNIP/JDBCResource/jdbc.TNIP')
cmo.setDatasourceType('GENERIC')


print ''
print '======================================================'
print 'The script has been send Password to the jdbc'
print '======================================================'
print ''

cd('/JDBCSystemResources/jdbc.TNIP/JDBCResource/jdbc.TNIP/JDBCDriverParams/jdbc.TNIP')
cmo.setUrl(dsURL)
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
set('Password', dsPassword)


print ''
print '======================================================'
print 'The script has been send setTestTableName to the Admin Server'
print '======================================================'
print ''

cd('/JDBCSystemResources/jdbc.TNIP/JDBCResource/jdbc.TNIP/JDBCConnectionPoolParams/jdbc.TNIP')
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')


print ''
print '======================================================'
print 'The script has been sent value intfwk_user '
print '======================================================'
print ''

cd('/JDBCSystemResources/jdbc.TNIP/JDBCResource/jdbc.TNIP/JDBCDriverParams/jdbc.TNIP/Properties/jdbc.TNIP')
cmo.createProperty('user')

cd('/JDBCSystemResources/jdbc.TNIP/JDBCResource/jdbc.TNIP/JDBCDriverParams/jdbc.TNIP/Properties/jdbc.TNIP/Properties/user')
cmo.setValue('tnipm')

print ''
print '======================================================'
print 'The script has been send setGlobalTransactionsProtocol '
print '======================================================'
print ''

cd('/JDBCSystemResources/jdbc.TNIP/JDBCResource/jdbc.TNIP/JDBCDataSourceParams/jdbc.TNIP')
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')


print ''
print '======================================================'
print 'The script has been sent value Targets '
print '======================================================'
print ''


cd('/JDBCSystemResources/jdbc.TNIP')
set('Targets',jarray.array([ObjectName('com.bea:Name=osb_cluster,Type=Cluster')], ObjectName))

save()
activate()
disconnect()


