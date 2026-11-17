

import pandas as pd
import asyncio
import aiohttp
import os

class Download_file:

    filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

    @staticmethod
    async def download(url, filename):

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:

                if response.status == 200:
                    content = await response.read()

                    with open(filename, "wb") as f:
                        f.write(content)

                    print("File downloaded successfully!")
                else:
                    print("Download failed:", response.status)


async def main():

    file_path = os.path.expanduser("~/Downloads/diabetes.csv")

    await Download_file.download(
        Download_file.filename,
        file_path
    )

    return file_path


file_path = asyncio.run(main())

df = pd.read_csv(file_path)

# Display complete table
print(df.to_string())

# Display table information
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)
