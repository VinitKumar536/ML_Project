# A pipeline is needed to make the whole ML process work in a fixed order without confusion.

# It takes data step by step—first collects it, then cleans and prepares it, then trains the model, and 
# finally checks results. Each step depends on the previous one, so nothing is skipped or done differently 
# each time. This saves time, avoids mistakes, and makes sure the same process runs every time, whether for
# practice or real use. Without a pipeline, everything becomes messy and hard to repeat.