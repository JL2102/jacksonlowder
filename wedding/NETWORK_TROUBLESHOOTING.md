# Network Access Troubleshooting

If your fiancé can't access the site from her phone, try these steps:

## ✅ Checklist

### 1. **Are you both on the same WiFi?**
- Your computer and her phone MUST be on the same WiFi network
- Not mobile data, not a different WiFi network
- Check WiFi name on both devices

### 2. **Run the firewall fix (Windows)**
1. Right-click on `allow_firewall.bat`
2. Select "Run as Administrator"
3. Press any key when it's done
4. Try accessing from phone again

### 3. **Get your correct IP address**
When you run `python start_server.py`, look for the line:
```
📱 Network access: http://192.168.X.XXX:8000
```

Make sure you're sharing the **Network access** URL, not the localhost URL!

### 4. **Test from your computer first**
On your computer, try opening the Network URL (the 192.168.X.XXX one) in your browser:
- If it works → firewall issue
- If it doesn't work → server issue

### 5. **Check if server is running**
Make sure the Python server window is still open and running. You should see:
```
🎉 Wedding Proposal Page Server Started!
```

Don't close this window while testing!

### 6. **Try a different port**
If port 8000 doesn't work, edit `start_server.py`:
- Change `PORT = 8000` to `PORT = 8080`
- Save and restart the server
- Use the new URL with `:8080` at the end

## 🔍 Common Issues

### "Site can't be reached" / "Connection refused"
- **Cause:** Firewall is blocking
- **Fix:** Run `allow_firewall.bat` as Administrator

### Wrong IP address
- **Cause:** Computer has multiple network adapters
- **Fix:** Check your IP manually:
  1. Open PowerShell
  2. Type: `ipconfig`
  3. Look for "Wireless LAN adapter" or "Ethernet adapter"
  4. Find "IPv4 Address" (looks like 192.168.X.XXX)
  5. Use that IP: `http://YOUR_IP:8000`

### Different networks
- **Cause:** Phone on different WiFi or mobile data
- **Fix:** Connect phone to same WiFi as your computer

### Public WiFi networks
- **Cause:** Some public/corporate WiFi blocks device-to-device communication
- **Fix:** Use your home WiFi or mobile hotspot

## 🆘 Alternative: Mobile Hotspot

If nothing works:

1. **Turn on Mobile Hotspot on YOUR phone**
2. **Connect your computer to your phone's hotspot**
3. **Connect your fiancé's phone to the same hotspot**
4. **Run the server again** (IP will change)
5. **Share the new Network URL**

## 📝 Quick Test Steps

1. ✅ Both on same WiFi?
2. ✅ Server running? (don't close the Python window)
3. ✅ Used the Network URL (192.168.X.XXX:8000)?
4. ✅ Ran firewall fix as Administrator?
5. ✅ Tested Network URL on YOUR computer first?

If all checked and still not working, try the Mobile Hotspot method!
