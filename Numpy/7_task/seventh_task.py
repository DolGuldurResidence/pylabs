import aiohttp
import asyncio

async def fetch_iris_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            iris_data = [row.split(",") for row in data.split("\n") if row]
            species_column = [row[4] for row in iris_data]
            return species_column

async def count_unique_species(species_column):
    unique_species = set(species_column)
    species_counts = {species: species_column.count(species) for species in unique_species}
    return unique_species, species_counts

async def main():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    species_column = await fetch_iris_data(url)
    unique_species, species_counts = await count_unique_species(species_column)
    print(f"Unique species: {unique_species}")
    print(f"Species counts: {species_counts}")

asyncio.run(main())