source("/Users/pengchen/hipy/rei/R_config.R")

system("aws s3 cp s3://pfc5098/rei/zhvi-single-family-by-city_long.csv .")

df <- read_csv("zhvi-single-family-by-city_long.csv") %>% 
  mutate(city_state = glue("{city}, {state}")) %>% 
  select(city_state, yr_mnth, price)

city_state_list <- c(
  "Columbia, MO", "New York, NY", "San Francisco, CA", "State College, PA"
)

df1 <- df %>% 
  filter(city_state %in% city_state_list) %>% 
  mutate(yr_mnth = yearmonth(yr_mnth)) %>% 
  as_tsibble(key = city_state, index = yr_mnth)

df1 %>% 
  rename(City = city_state) %>% 
  autoplot(.vars = price, size = 0.78) +
  scale_y_continuous(label = dollar) + 
  labs(title = "House price", x = "", y = "", color = "City") + 
  theme_light()
