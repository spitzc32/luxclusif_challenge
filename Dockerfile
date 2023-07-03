FROM bitnami/spark:3-debian-10
USER root
WORKDIR /opt/app
ADD requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# USER 185
#Copy python script for batch
ENV WORKDIR=/app
WORKDIR ${WORKDIR}

# Copy content from current directory into image
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/code/src"
CMD python3 $WORKDIR/src/main.py