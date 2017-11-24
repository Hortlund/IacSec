=begin
Akond Rahman
Nov 24, 2017
See if path values contain anti-patterns
=end
PuppetLint.new_check(:no_hardcode_key) do

  def check
       resource_indexes.each do |resource|
           resource[:param_tokens].each do |param_token|
               value_token   = param_token.next_code_token.next_code_token
               token_val_str = value_token.value
               path_sym_cnt1  = token_val_str.count('/')
               path_sym_cnt2  = token_val_str.count('\\')
               #print "#{path_sym_cnt} \n"
               ##first check if value is a directory or file, if valeu contains at least two slashes then proceed
               if path_sym_cnt1 > 1 or path_sym_cnt2 > 1
                  print "#{token_val_str} \n"
               end
           end
       end
  end
end
