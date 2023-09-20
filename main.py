from data_ingestion import FileSystemReader, CloudStorageReader, DatabaseReader, DataIngester

file_reader = FileSystemReader()
s3_reader = CloudStorageReader()
db_reader = DatabaseReader()

ingester = DataIngester({"file": file_reader, "s3": s3_reader, "db": db_reader})

data = ingester.ingest("file:data/file.txt")
print(data)
