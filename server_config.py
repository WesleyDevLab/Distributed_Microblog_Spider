__author__ = 'multiangle'

#=======    USED IN server_proxy.py    ====================================
GET_PROXY_URL                   ='http://vxer.daili666api.com/ip/?tid=559' \
                                '842334303001&num={NUM}&operator=1&category=2&foreign=none'
PROXY_POOL_SIZE                 =600
VERIFY_PROXY_THREAD_NUM         =300
PROXY_PATH                      ='proxy\\'         # the folder path where raw and checked proxy is stored
PROXY_NORMAL_INFO_PRINT         =True
MAX_VALID_PROXY_THREAD_NUM      =3
PROXY_MONITOR_GAP               =10        # （seconds） every 10 seconds, a process will note the state
                                            #               proxy pool
PROXY_SIZE_STATE_LIST_LEN       =30    #the len of proxy size state list. For example if you want
                                        #   to monitor the state of proxy pool in latest 5 minutes,
                                        #   the value of this item be 60*5/PROXY_MONITOR_GAP
HISTORY_TASK_VALVE              =15000      # 微博数大于15000的，由本机完成搜索，小于15000的，交由云主机