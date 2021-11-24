#!/bin/sh
i=0
while [ $i -lt 10 ]
do
    /usr/bin/time -f "%e" -a -o output.txt ${SPARK_HOME}/bin/spark-submit --master spark://spark-master-svc:7077 --properties-file ${SPARK_HOME}/conf/spark-driver.conf ${SPARK_HOME}/mapreduce.py
    i=`expr $i + 1`
done
