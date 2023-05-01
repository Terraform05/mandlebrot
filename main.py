from multiprocessing_mandlebrot import mp_timing_mandlebrot
from reg_mandlebrot import reg_timing_mandlebrot
from multiprocessing import cpu_count
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint


def ns_s(ns):
    return ns/1e9

def calculate(start,stop,step):
    times_df = [[i] for i in range(1, cpu_count()+1)]  # [1,2,3,4,5,6,7,8
    
    #create list of aryNN values
    aryNN_list = [i for i in range(start,stop,step)]
    print(aryNN_list)
   
    #create list of times for each aryNN value
    for c in times_df:
        core = c[0]
        for n in aryNN_list:
            reg_time = reg_timing_mandlebrot(n)
            mp_time = mp_timing_mandlebrot(n, core)
            c.append(reg_time/mp_time)
        
        
        
        print(c)
    
    #add zero core time
    zero_cores = [0]
    for i in range(len(aryNN_list)):
        zero_cores.append(0.0)
    times_df.insert(0, zero_cores)
    
    #to dataframe
    su_df = pd.DataFrame(times_df, columns=['cpu cores (p)'] + aryNN_list)
    su_df.set_index('cpu cores (p)', inplace=True)
    print(su_df)
    
    #save to csv
    su_df.to_csv('su_df.csv')
    
    #efficiency
    for core in range(len(times_df)):
        for col in range(core[0][1:]):
            times_df[core][col]/core[0]
    ef_df = pd.DataFrame(times_df, columns=['cpu cores (p)'] + aryNN_list)
    ef_df.set_index('cpu cores (p)', inplace=True)
    print(ef_df)
    
    ef_df.to_csv('ef_df.csv')
    
    
    plot(su_df, 'cpu cores (p)', 'Speedup', 'Speedup vs. CPU Cores (p)')
    plot(ef_df, 'cpu cores (p)', 'Efficiency', 'Efficiency vs. CPU Cores (p)')
            
    
    
    
def use_csv():
    #read csv
    su_df = pd.read_csv ('su_df.csv', index_col=0)
    ef_df = pd.read_csv ('ef_df.csv', index_col=0)
    print(su_df)
    print('='*80)
    print(ef_df)    
    plot(su_df, 'cpu cores (p)', 'Speedup', 'Speedup vs. CPU Cores (p)')
    plot(ef_df, 'cpu cores (p)', 'Efficiency', 'Efficiency vs. CPU Cores (p)')
    
def plot(df, xlabel, ylabel, title):
    plt.cla()
    # matplotlib
    ax = df.plot(title = title, figsize=(16, 8), ax = None)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.axhline(y=0, color='black')
    ax.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    
    use_downloaded_csv = False
    
    if use_downloaded_csv:
        use_csv()
    else:
        calculate(600,1200,100)
   
