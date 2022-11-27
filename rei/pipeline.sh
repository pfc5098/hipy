working_dir=/Users/pengchen/hipy/rei

cd ${working_dir}

echo "Downlod raw data from s3."
aws s3 cp s3://pfc5098/rei/zhvi-single-family-by-city.csv .

echo "Transform data to timeseries format."
Rscript convert_to_timeseries.R

echo "Upload transformed data to s3."
aws s3 cp zhvi-single-family-by-city_long.csv s3://pfc5098/rei/zhvi-single-family-by-city_long.csv

echo "Clean up."
rm *.csv

# linear analysis by state
