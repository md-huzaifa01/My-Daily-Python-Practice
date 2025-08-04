# Write code using find() and string slicing (see section 6.10) to extract the number at--
# ---the end of the line below. Convert the extracted value to a floating point number--
# --and print it out from this. (text = "X-DSPAM-Confidence:    0.8475")
tx = "X-DSPAM-Confidence: 0.8475"
x= tx.find(":")
number_str = tx[x + 1:].strip()
numf= float(number_str)
print(numf)
