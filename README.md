# Rosee


Traceback (most recent call last):
  File "C:\Users\Acer\Downloads\roseeai\rosee-ai\rosee.py", line 8, in <module>
    model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-llm-7b-chat", device_map="auto", torch_dtype=torch.float16)
  File "C:\Users\Acer\AppData\Roaming\Python\Python313\site-packages\transformers\models\auto\auto_factory.py", 
line 573, in from_pretrained
    return model_class.from_pretrained(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        pretrained_model_name_or_path, *model_args, config=config, **hub_kwargs, **kwargs
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\Acer\AppData\Roaming\Python\Python313\site-packages\transformers\modeling_utils.py", line 272, 
in _wrapper
    return func(*args, **kwargs)
  File "C:\Users\Acer\AppData\Roaming\Python\Python313\site-packages\transformers\modeling_utils.py", line 4203, in from_pretrained
    raise ImportError(
        f"Using `low_cpu_mem_usage=True`, a `device_map` or a `tp_plan` requires Accelerate: `pip install 'accelerate>={ACCELERATE_MIN_VERSION}'`"
    )
ImportError: Using `low_cpu_mem_usage=True`, a `device_map` or a `tp_plan` requires Accelerate: `pip install 'accelerate>=0.26.0'`
