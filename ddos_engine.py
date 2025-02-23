import pandas as pd
from scapy.all import *

warnings.filterwarnings("ignore")
import joblib


#
# print('The scikit-learn version is {}.'.format(sklearn.__version__))

def load_model():
    model_filename = 'random_forest_model.pkl'
    scaler_filename = 'standard_scaler.pkl'
    # Load the trained model and StandardScaler from the files
    loaded_model = joblib.load(model_filename)
    loaded_scaler = joblib.load(scaler_filename)
    return loaded_model, loaded_scaler


loaded_model, loaded_scaler = load_model()


def predict(packet_filename):
    # Load packets from the custom PCAP file
    packets = rdpcap(packet_filename)

    # Initialize an empty list to store the extracted data
    data_list = []

    # Iterate through each packet and extract the necessary fields
    for packet in packets:
        if Raw in packet:
            raw_layer = packet[Raw].load

            dt = struct.unpack(">I", raw_layer[:4])[0]
            switch = struct.unpack(">I", raw_layer[4:8])[0]
            src = raw_layer[8:24].rstrip(b'\x00').decode("utf-8")
            dst = raw_layer[24:40].rstrip(b'\x00').decode("utf-8")
            pktcount = struct.unpack(">I", raw_layer[40:44])[0]
            bytecount = struct.unpack(">I", raw_layer[44:48])[0]
            dur = struct.unpack(">f", raw_layer[48:52])[0]
            dur_nsec = struct.unpack(">I", raw_layer[52:56])[0]
            tot_dur = struct.unpack(">f", raw_layer[56:60])[0]
            flows = struct.unpack(">I", raw_layer[60:64])[0]
            packetins = struct.unpack(">I", raw_layer[64:68])[0]
            pktperflow = struct.unpack(">I", raw_layer[68:72])[0]
            byteperflow = struct.unpack(">I", raw_layer[72:76])[0]
            pktrate = struct.unpack(">I", raw_layer[76:80])[0]
            Pairflow = struct.unpack(">I", raw_layer[80:84])[0]
            Protocol = raw_layer[84:100].rstrip(b'\x00').decode("utf-8")
            port_no = struct.unpack(">H", raw_layer[100:102])[0]
            tx_bytes = struct.unpack(">I", raw_layer[102:106])[0]
            rx_bytes = struct.unpack(">I", raw_layer[106:110])[0]
            tx_kbps = struct.unpack(">I", raw_layer[110:114])[0]
            rx_kbps = struct.unpack(">I", raw_layer[114:118])[0]
            tot_kbps = struct.unpack(">I", raw_layer[118:122])[0]

            # Create a dictionary with the extracted fields
            data_dict = {
                'dt': dt,
                'switch': switch,
                'src': src,
                'dst': dst,
                'pktcount': pktcount,
                'bytecount': bytecount,
                'dur': dur,
                'dur_nsec': dur_nsec,
                'tot_dur': tot_dur,
                'flows': flows,
                'packetins': packetins,
                'pktperflow': pktperflow,
                'byteperflow': byteperflow,
                'pktrate': pktrate,
                'Pairflow': Pairflow,
                'Protocol_ICMP': 1 if Protocol == 'ICMP' else 0,
                'Protocol_TCP': 1 if Protocol == 'TCP' else 0,
                'Protocol_UDP': 1 if Protocol == 'UDP' else 0,
                'port_no': port_no,
                'tx_bytes': tx_bytes,
                'rx_bytes': rx_bytes,
                'tx_kbps': tx_kbps,
                'rx_kbps': rx_kbps,
                'tot_kbps': tot_kbps,
            }

            # Append the dictionary to the data list
            data_list.append(data_dict)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    # Get the feature names used during training
    original_feature_names = loaded_scaler.feature_names_in_
    # Now, 'df' contains the extracted fields in the same order as your desired DataFrame
    # print(df)
    labels = ["The request is a DDOS attack", "The request is not a DDOS attack"]
    X = df.drop(['dt', 'src', 'dst'], axis=1)

    # Rearrange the columns in 'X' to match the original feature order
    X_reordered = X[original_feature_names]

    # Transform the new data using the loaded scaler
    scaled_new_data = loaded_scaler.transform(X_reordered)

    # Ensure that the column names match the feature names
    scaled_new_df = pd.DataFrame(scaled_new_data, columns=original_feature_names)

    # Predict using the loaded model
    predicted_labels = loaded_model.predict(scaled_new_df)

    # Print the predicted labels
    # print(predicted_labels)

    info = ''
    i = 1
    for key, value in data_dict.items():
        if i % 2 == 0:
            info += key + ' : ' + str(value) + '\n '
        else:
            info += key + ':' + str(value) + ', '
        i += 1
    return info, labels[int(predicted_labels)]