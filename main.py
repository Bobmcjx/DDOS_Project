from ddos_engine import predict

pred = predict('malicious.pcap')
print(pred)
pred = predict('benign.pcap')
print(pred)