import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import math, os, numpy


def get_datetime_from_report(report, datetime):
    timestamp = report.find('timestamp')
    return(timestamp.find(datetime).text)
    
def get_temp_from_report(report, dev):
    hdc = report.find(dev)
    temp = hdc.find('t').text
    temp = temp.replace(',', '.')
    return (float(temp))    

def get_list_files(file_name):
    # Set path to data file
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_path = current_path + '\\data'
    dir_list = os.listdir(data_path)
    file_list = os.listdir(data_path + '\\' + dir_list[0])

    file_list.sort()
    idx = 0
    for (i, file) in enumerate(file_list):
        if (file_name in file):
            print ('file: ' + file)
            idx = i
            break;
    print(idx)
    del file_list[0:idx]
    return file_list
    
def show_temp_graph(path):
    tree = ET.parse(path)
    root = tree.getroot()

    x_tick = [] # x ticks like 10:42:30:513, 10:42:31:513 and etc
    hdc_temp = [] # temperature from hdc1080  
    lps_temp = [] # temperature from lps331

    for report in root:
        # Get node timestamp for x_ticks
        x_tick.append(get_datetime_from_report(report, 'time')[:-4])
        # Get temp from hdc1080 node
        hdc_temp.append(get_temp_from_report(report, 'hdc1080'))
        # Get temp from lps331 node
        lps_temp.append(get_temp_from_report(report, 'lps331'))

    # Create plots
    fig, ax = plt.subplots()
    plt.title("Temperature graphic", fontsize = 14)
    plt.xlabel("Time", fontsize = 8)
    plt.ylabel("Temperature", fontsize = 12)
    # Generate a list from 0 to report number
    x = [++i for i in range(len(root))]
    ax.plot(x, hdc_temp, 'r-', label='hdc_temp')
    ax.plot(x, lps_temp, 'y-', label='lps331')

    # Create x_tick, grid and legend
    plt.xticks(x, x_tick, rotation = 90)
    plt.grid(linestyle = 'dashed')
    legend = ax.legend(loc='best')

    # Set the origin
    y_mean = numpy.mean(hdc_temp)
    ax.axhline(y = y_mean - y_mean/10, color = 'k')
    ax.axvline(x = 0, color = 'k')

    # Set fig to fullscreen
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    plt.show()
    
def show_acc_graph(path):
    tree = ET.parse(path)
    root = tree.getroot()

    # x_tick = [] # x ticks like 10:42:30:513, 10:42:31:513 and etc
    x = [] # acc for axis
    y = [] # acc for axis
    z = [] # acc for axis
    
    print(root)
    # get node data
    reports = root.find('report')
    print(reports)
    for report in reports:
        print(report)
    #    # Get node timestamp for x_ticks
    #    x_tick.append(get_datetime_from_report(report, 'time')[:-4])
    #    # Get temp from hdc1080 node
    #    x.append(get_temp_from_report(report, 'hdc1080'))
    #    # Get temp from lps331 node
    #    lps_temp.append(get_temp_from_report(report, 'lps331'))    
 
    
def show_graph(path):
    if not os.path.isfile(path):
        return
    if 'acc_report' in path:
        show_acc_graph(path)
    if 'tph_report' in path:
        show_temp_graph(path)


def main():
    # fl = get_list_files('tph_report')
    fl = get_list_files('acc_report')
    print(fl)
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_path = current_path + '\\data'
    dir_list = os.listdir(data_path)
    path = data_path + '\\' + dir_list[0] + '\\' + fl[0]
    print(path)
    show_graph(path)
    

if __name__ == '__main__':
    main()