FILE forge.yaml
registry:
  type: docker
  url: registry.hub.docker.com
  namespace: forgeorg
END

RUN docker login registry.hub.docker.com -u forgetest -p forgetest

FILE k8s/subdir/DUMMY
END

FILE k8s/blah.yaml
---
apiVersion: v1
kind: Service
metadata:
  name: {{build.name}}
spec:
  ports:
  - protocol: TCP
    port: 80
END

FILE service.yaml
name: manifest-subdir
END

RUN forge deploy
RUN kubectl get svc manifest-subdir-default
