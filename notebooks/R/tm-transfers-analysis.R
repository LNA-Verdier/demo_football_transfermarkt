library("arrow")
library("ggplot2")
library("dplyr")

dataset <- open_dataset(
  s3_bucket(
    "loicverdier/gold/football_transfermarkt/transfers_balance",
    endpoint_override = "https://minio.lab.sspcloud.fr",
    access_key = Sys.getenv("AWS_ACCESS_KEY_ID"),
    secret_key = Sys.getenv("AWS_SECRET_ACCESS_KEY"),
    session_token = Sys.getenv("AWS_SESSION_TOKEN"),
    scheme = "https",
    anonymous = FALSE
  ),
  format = "parquet"
)

df <- as.data.frame(dataset)

top_20 <- df %>%
  arrange(desc(total_purchases)) %>%
  slice_head(n = 20)

top_20 <- top_20 %>%
  mutate(club_year = paste0(club_name, " (", transfer_year, ")"))

ggplot(top_20, aes(x = reorder(club_year, total_purchases), y = total_purchases, fill = club_name)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(
    title = "Top 20 club/année par dépenses",
    x = "Club (Année)",
    y = "Total achats (€)"
  ) +
  theme_minimal()
