#!/bin/sh
# Configure module
set -e

mkdir -p /opt/jboss/container/jolokia/etc
chmod 775 /opt/jboss/container/jolokia/etc
chown -R jboss:root /opt/jboss/container/jolokia/etc
