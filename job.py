from img2dataset import download
from img2dataset.reader import Reader


# reader = Reader(url_list="shopify_products_10k.parquet",
#     input_format="parquet",
#     url_col="product_image_224",
#     caption_col="product_title",
#     save_additional_columns=['shopify_id', 'domain', 'shop_description', 'product_image', 'product_image_basename', 'product_type', 'vendor', 'product_description'],
#     number_sample_per_shard=1000,
#     done_shards = set(),
#     tmp_path = "dataset_01_10k/_tmp"
# )
# 
# for i, (shard_id, shard_path) in enumerate(reader):
#     print(i, shard_id, shard_path)

if __name__ == '__main__':
    download(
        processes_count=1,
        # thread_count=32,
        url_list="shopify_products_10k.parquet",
        image_size=224,
        output_folder="s3://embedder/",
        output_format="files",
        input_format="parquet",
        url_col="product_image_224",
        enable_wandb=False,
        number_sample_per_shard=10000,
        distributor="multiprocessing",
        caption_col="product_title",
        save_additional_columns=['shopify_id', 'domain', 'shop_description', 'product_image', 'product_image_basename', 'product_type', 'vendor', 'product_description'],
    )