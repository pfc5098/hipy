source("/Users/pengchen/hipy/rei/R_config.R")

df <- fread("zhvi-single-family-by-city.csv") %>% as_tibble()

col2rm <- c("RegionID", "SizeRank", "RegionType", "StateName", "Metro", "CountyName")

df1 <- df %>% 
  select(!any_of(col2rm)) %>% 
  pivot_longer(cols = -c(1, 2), names_to = "yr_mnth", values_to = "price", values_drop_na = TRUE) %>% 
  clean_names() 

df2 <- df1 %>% 
  mutate(yr_mnth = ymd(yr_mnth)) %>% 
  rename(city = region_name)

fwrite(df2, "zhvi-single-family-by-city_long.csv")


