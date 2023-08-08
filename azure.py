def re_arrange_partition_column(input_df, partition_column):
  column_list = []
  for column_name in input_df:
    if column_name != partition_column:
      column_list.append(column_name)
  column_list.append(partition_column)
  output_df = input_df.select(column_list)
  return output_df


print(re_arrange_partition_column(['a','b','c'],['c']))

#InputValue = [111,222,222,333,333]
#WinLotto = [222,333]