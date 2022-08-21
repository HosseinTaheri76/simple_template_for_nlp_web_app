
import torch
from datasets import Dataset
from helper_bert2bert import Helper

helper = Helper("./checkpoint-18138", do_tr_lowercase=False, source_prefix="",
                       max_source_length=512,
                       max_target_length=120, num_beams=4, ngram_blocking_size=3, early_stopping=None,
                       use_cuda=torch.cuda.is_available(),
                       batch_size=1, language="fa")

text = '''متن خبر'''.replace('\n', '')

inp_dict = {"input": [text]}
test_data = Dataset.from_dict(inp_dict)
test_data = test_data.map(
    helper.preprocess_function,
    batched=True,
    load_from_cache_file=False
)
result = test_data.map(helper.generate_summary, batched=True, batch_size=helper.batch_size,
                        load_from_cache_file=False)

print({"summary": result['predictions'][0]})

