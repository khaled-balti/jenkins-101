import fire

def hello(name="World"):
  return "Hello to %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
