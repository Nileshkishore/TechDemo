#!/bin/bash

# Delete metrics collector deployment
kubectl delete -f kubernetes/metrics.yaml

# Delete Grafana deployment and ConfigMap
kubectl delete -f kubernetes/grafana.yaml

# Delete Prometheus deployment and ConfigMap
kubectl delete -f kubernetes/prometheus.yaml

# Delete frontend deployment
kubectl delete -f kubernetes/frontend.yaml

# Delete backend deployment
kubectl delete -f kubernetes/backend.yaml

# Delete PostgreSQL deployment and PVC
kubectl delete -f kubernetes/database.yaml

# Delete the namespace
kubectl delete -f kubernetes/namespace.yaml
