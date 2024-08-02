#!/bin/bash

# Apply the namespace
kubectl apply -f kubernetes/namespace.yaml

# Apply PostgreSQL deployment and PVC
kubectl apply -f kubernetes/database.yaml

# Apply backend deployment
kubectl apply -f kubernetes/backend.yaml

# Apply frontend deployment
kubectl apply -f kubernetes/frontend.yaml

# Apply Prometheus deployment and ConfigMap
kubectl apply -f kubernetes/prometheus.yaml

# Apply Grafana deployment and ConfigMap
kubectl apply -f kubernetes/grafana.yaml

# Apply metrics collector deployment
kubectl apply -f kubernetes/metrics.yaml
