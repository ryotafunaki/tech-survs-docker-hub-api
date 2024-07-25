# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
import argparse
import asyncio

from api.helpers.repo_client import RepoClient, RepoInfo


async def main():
    parser = argparse.ArgumentParser(
        prog="python run main.py"
    )
    parser.add_argument("-n", "--namespace", type=str,
                        help="Docker Hub namespace")
    parser.add_argument("-r", "--repository", type=str,
                        help="Docker Hub repository")
    parser.add_argument("-t", "--tag", type=str, help="Docker Hub tag")
    args = parser.parse_args()

    client = RepoClient()
    repo_info = RepoInfo()
    repo_info.namespace = args.namespace
    repo_info.repository = args.repository
    repo_info.tag = args.tag
    response = await client.get_info(repo_info)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
