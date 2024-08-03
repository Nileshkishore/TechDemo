#!/bin/bash

kubectl port-forward -n stock-monitoring svc/backend 8001:8000 &
kubectl port-forward -n stock-monitoring svc/db 8002:5432 &
kubectl port-forward -n stock-monitoring svc/frontend 8003:3000 &
kubectl port-forward -n stock-monitoring svc/grafana 8004:3000 &
kubectl port-forward -n stock-monitoring svc/metrics-collector 8005:7878 &
kubectl port-forward -n stock-monitoring svc/prometheus 8006:9090 &
