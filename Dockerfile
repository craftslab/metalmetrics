FROM python:3.9.0 as build-stage
WORKDIR /usr/src/app
COPY . .
RUN apt update && \
    apt install -y upx
RUN wget https://github.com/smxi/inxi/archive/3.2.02-2.zip && \
    unzip 3.2.02-2.zip && \
    mv inxi-3.2.02-2/inxi .
RUN make install

FROM nginx as production-stage
WORKDIR /usr/dist/bin
RUN mkdir -p /usr/dist/bin
COPY --from=build-stage /usr/src/app/dist/* ./
COPY --from=build-stage /usr/src/app/inxi ./
COPY --from=build-stage /usr/src/app/metalmetrics/config/*.yml ./
