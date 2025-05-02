from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PySpark SQL Training") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

# Test the session
test_df = spark.createDataFrame([
    (1, "Test"),
    (2, "Data")
], ["id", "value"])

# Show the test data
test_df.show()

# When you're done, stop the session
# Properly stop the SparkSession
spark.stop()

