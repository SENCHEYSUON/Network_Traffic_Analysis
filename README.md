<h1 align="center">Wireshark Crash Course</h1>

**Disclaimer:** Some of the pcap files are from the internet and a few of them I captured at my university. I have just done simple password sniffing and understand how dangerous accessing HTTP via public Wi-Fi can be. (Disclaimer: For educational purposes only)

## Inspecting Network Traffic using Wireshark

Wireshark is a free and open-source packet analyzer that allows you to see what's happening on your network at a microscopic level. With Wireshark, you can capture network traffic in real time and analyze it to troubleshoot network issues, detect security vulnerabilities, and optimize network performance.

### What is Wireshark?

Wireshark is a network protocol analyzer that captures packets and displays their details in a user-friendly interface. It supports a wide range of protocols, including TCP, UDP, HTTP, DNS, and many more. Wireshark is available for Windows, macOS, and Linux, and it can capture traffic from both wired and wireless networks.

### How does Wireshark work?

Wireshark captures packets by putting the network interface card (NIC) into promiscuous mode. In this mode, the NIC captures all traffic on the network, regardless of its intended recipient. Wireshark then decodes and analyzes the packets, displaying their details in a hierarchical tree-like structure. You can drill down into each packet to see its various fields, such as source and destination IP addresses, protocol type, packet length, and much more.

## Network Traffic Analysis

1. **Analyze the traffic.pcapng file; find the IP address of the DNS server.**
   - **Answer:** 10.103.0.20
   - **Solution:** `dns`

2. **Analyze the network file and find the destination port number used to communicate with the DHCP server.**
   - **Answer:** 67
   - **Solution:** `dhcp`

3. **Analyze the network file and find the DHCP server IP address.**
   - **Answer:** 10.103.0.20
   - **Solution:** `dhcp`

4. **Analyze the network file and find the IP address used by the MAC address 64:31:50:2c:3e:d2.**
   - **Answer:** 10.103.0.70
   - **Solution:** `eth.addr == 64:31:50:2c:3e:d2`

5. **Analyze the network file and find the IP address related to the pastebin.com domain.**
   - **Answer:** 104.23.98.190
   - **Solution:** `dns.qry.name == pastebin.com`

6. **Analyze the network file and find the network card vendor of 10.103.230.1.**
   - **Answer:** MicroStarINT_75
   - **Solution:** `ip.addr == 10.103.230.1 and eth.addr`

7. **Analyze the network file and find the port number used to access the 'pastebin.com' website.**
   - **Answer:** 53
   - **Solution:** `https (dns.qry.name == pastebin.com)`

8. **Analyze the network file and find the port number used to access the Telnet server.**
   - **Answer:** 23
   - **Solution:** `telnet`

9. **Analyze the network file and find the Telnet server IP address.**
   - **Answer:** 12.0.1.28
   - **Solution:** `telnet`

10. **Analyze the network file and find the number of packets it contains.**
    - **Answer:** 26456
    - **Solution:** No filter anything just look at the bottom right.

11. **Analyze the network file and find the number of seconds the network was recorded.**
    - **Answer:** 348
    - **Solution:** No filter just see the last packet.

12. **Analyze the network file and filter for DNS; find the number of displayed packets.**
    - **Answer:** 469
    - **Solution:** `dns`

13. **Analyze the network file and find the password used to access the Telnet service.**
    - **Answer:** Rviews
    - **Solution:** telnet and at the bottom one click, follow => TCP Stream

14. **Analyze the network file and find the IP address that sent the most packets.**
    - **Answer:** 10.103.51.159
    - **Solution:** statistics => endpoint => ipv4 or statistic => ipv4 statistics => all address

15. **Run Wireshark and listen to the network; ping 8.8.8.8 and find the protocol name displayed.**
    - **Answer:** ICMP
    - **Solution:** first open Wireshark, cmd, choose wifi and run the ping 8.8.8.8 in cmd and after finish filter ip.addr == 8.8.8.8

16. **Analyze the network file traffic2.pcap and find the Broadcast MAC address.**
    - **Answer:** ff:ff:ff:ff:ff:ff
    - **Solution:** `eth.dst and arp`

17. **Filter the network file for the string 'favicon'; what protocol is used in the filtered packets?**
    - **Answer:** HTTP
    - **Solution:** `frame contains "favicon"`

18. **Filter the network file for HTTP and identify the public IP address that sent the highest number of packets.**
    - **Answer:** 46.21.248.221
    - **Solution:** http => Statistic => conversion, ipv4

19. **Open the network file and find the number of packets that were sent from the IP '109.70.100.4'.**
    - **Answer:** 28
    - **Solution:** ip.addr == 109.70.100.4, statistic, conversion

20. **Filter the network file for TCP port 80; inspect the TCP stream of the first packet and find the Server's service.**
    - **Answer:** Microsoft-IIS/8.5
    - **Solution:** tcp.port == 80, find the first click follow, tcp stream
21. **Analyze the traffic(1).pcapng file; find the number of DHCP messages.**
    - **Answer:** 5
    - **Solution:** `dhcp`

22. **Analyze the network file and find the number of ARP messages.**
    - **Answer:** 680
    - **Solution:** `filter arp and see the displayed packets.`

23. **Analyze the network file and find the IP address that accessed 'baidu.com'.**
    - **Answer:** 10.103.51.159
    - **Solution:** `frame contains "baidu.com"`

24. **Analyze the network file and find the number of packets the IP address 10.103.0.20 sent.**
    - **Answer:** 469
    - **Solution:** `ip.addr == 10.103.0.20, then Statistics then Conversions then IPv4.`

25. **Analyze the network file and find the number of UDP packets.**
    - **Answer:** 9102
    - **Solution:** `udp`

26. **Analyze the network file and find the number of SMB packets.**
    - **Answer:** 518
    - **Solution:** `smb`

27. **Analyze the network file and find the number of packets sent to the source IP address 10.103.0.20.**
    - **Answer:** 547
    - **Solution:** `ip.dst == 10.103.0.20, then IPv4, then Packets A -> B`

28. **Examine the network file and isolate only the IPv4 traffic; determine the count of packets shown.**
    - **Answer:** 24906
    - **Solution:** `No filter, Then Statistics, then IPv4 statistics, then All addresses`

29. **Analyze the network file and examine the last SMB packet; identify the source IP address.**
    - **Answer:** 10.103.50.202
    - **Solution:** `smb then see the last packet.`

30. **Analyze the network file and find the MAC address of the IP 151.139.128.14.**
    - **Answer:** 00:1c:7f:6c:96:3f
    - **Solution:** `ip.addr == 151.139.128.14 then see the mac address in the Ethernet II.`

31. **Examine packet 416 in the network file and identify the protocol being used.**
    - **Answer:** DNS
    - **Solution:** `frame.number == 416`

32. **Examine packet 416 in the network file and identify the destination IP address.**
    - **Answer:** 10.103.0.20
    - **Solution:** `frame.number == 416`

33. **Examine packet 416 in the network file and identify the destination IP address.**
    - **Answer:** 10.103.51.159
    - **Solution:** `frame.number == 416`

34. **Examine the network file and analyze the first HTTP packet; what is the source port?**
    - **Answer:** 64079
    - **Solution:** `http, then in the TCP see Src Port.`

35. **Analyze the network file and find the duration of the capture (in seconds).**
    - **Answer:** 348
    - **Solution:** `no filter anything see the last packet.`

36. **Analyze the network file and find the number of NBNS packets.**
    - **Answer:** 963
    - **Solution:** `nbns then see the Displayed packets.`

37. **Analyze the network file and find the number of TCP packets sent with source port 443.**
    - **Answer:** 7275
    - **Solution:** `tcp.srcport == 443`

38. **Examine the network file and find the number of TCP packets sent to destination port 443.**
    - **Answer:** 5966
    - **Solution:** `tcp.dstport == 443`

39. **Examine the network file; what is the number of packets sent to the destination IP address 204.79.197.200?**
    - **Answer:** 116
    - **Solution:** `ip.dst == 204.79.197.200`

40. **Analyze the network file and find the MAC address associated with the IP address 204.79.197.200. To which vendor does this MAC address belong?**
    - **Answer:** Check Point Software Technologies
    - **Solution:** `filter ip.addr == 204.79.197.200 then see the MAC address of the Dst: 00:1c:7f:6c:96:3f then go to https://dnschecker.org/mac-lookup.php enter the mac address, see the Vendor / Company.`

