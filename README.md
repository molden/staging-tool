# staging-tool
This tools helps you to keep track of your data over different storage tiers.

Actually this tool is doing the same as:

```bash
rsync -i -u -r --dry-run <PATH_to_archive/archive_folder> <PATH_to_scratch/archive_folder>
```

## Use

Let's say there is an archive storage tier from which you want to stage data to your scratch storage space. You should first copy the data folder using this command:

```bash
rsync -a <PATH_to_archive/archive_folder> <PATH_to_scratch>
```

This will create the folder PATH_to_scratch/archive_folder with all content from folder PATH_to_archive/archive_folder preserving all metada like modification time and permissions.

Now you will want to track the changes you make to any content in PATH_to_scratch/archive_folder. So that at some point in time, when you need to copy back the data to archive, you can only copy back the changed content. You can track your data using this command:

```bash
 ./src/track_my_data.py --origin <PATH_to_archive/archive_folder> --destination <PATH_to_scratch/archive_folder>
```

Note: you should execute this command right after you copied your data using rsync.

Now you can modify the data in PATH_to_scratch/archive_folder and when you are ready to copy your modified data back to archive you can execute this command:

```bash
 ./src/verify-metadata.py --origin <PATH_to_archive/archive_folder> --local <PATH_to_scratch/archive_folder>
```

This will give you an overview of all the files and/or directories that changed since tracking your data. This list of files are the only files you will need to copy back to your archive.

## dependencies

This tools depends on https://github.com/molden/MetadataExporter : add the src directory to your PYTHONPATH.
