# lambda_xregion_copy
This is a lambda script to copy volume snapshots from one region to another

As the Lifecycle Manager is leaving 5 last days, It will copy only snapshots that were created today to prevent problems with copy the same snapshot. The script will check for the date of the snapshot and compare it with todays date
