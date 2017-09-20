*Downloader framework*
Create a basic downloader framework that allows downloading data on a daily basis from a predetermined location at a regular time everyday. Basically in the input config, the following would be provided
1. IP and ssh Login details of server on which data resides.
2. Location of the source data
3. Destination of downloaded data
4. Time window(download has to start within this window and to be closed after the window ends)

Also print warning messages if the raw data could not be downloaded because of some reason.


#start_time,end_time,user,ip,source_path,destination_path
