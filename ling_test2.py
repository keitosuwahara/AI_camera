import transformers 
from transformers import BertConfig, BertJapaneseTokenizer, BertForMaskedLM
from transformers import pipeline

config = BertConfig.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
model = BertForMaskedLM.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
fill_mask = pipeline('fill-mask', model=model, tokenizer=tokenizer, config=config)
#print(fill_mask('誕生日に[MASK]を食べるのが楽しみだ。'))
#print(fill_mask('校庭に[MASK]が入ってきて、皆大騒ぎだ。'))
#print(fill_mask('将来は、[MASK]になるのが夢だ。'))
#print(fill_mask('太郎は、[MASK]部のエースだ。'))
print(fill_mask('山の上に、[MASK]があるように見える。'))