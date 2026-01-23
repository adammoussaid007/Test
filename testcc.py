import requests
import asyncio
import aiohttp


url = 'https://backboard.railway.com/graphql/internal?q=serviceDomainCreate'
headers = {
    'authority': 'backboard.railway.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'content-type': 'application/json',
    'cookie': '_gcl_au=1.1.185931791.1769181974; IndrX0xRN0EzRW5rX0RpMmQ2MUM3N3dNR0x5ZzhzMTQ2aEM3WFpxUWVVNDZtX2Fub255bW91c1VzZXJJZCI%3D=IjNiNjQ1ZGQ2LTJkYzgtNDRkNy04ZmVmLTJiNzU2MDE3NzY5OSI=; osano_consentmanager_uuid=2a3e90a2-746e-42ee-92e5-071c0c944b4f; osano_consentmanager=xwW2MVW_05D8Pi1fhili26kmlcv07ZKcbvGlrBqxsW_sxEO6xPuPCU9NGwBQVE3nSbCY0iRTc1HCywmdSlo5oI2c9japHHC0I8hYBThJrQKG6EF84STUMFRlJxZ8VkbLnobxIfFjxqo7O6k8EYTmLQ0foxhPIp67Ukq6NE1Ibsu00J58wEHCgcFPb8raYWqaL_xdlB2GkXoodr5vlXOpEPZZYLaO1yeNSUeK6JJoZaqpkf-mKvnHnZ7mWPLE1dGzYhu1f8W0WEq7V9GABGXUTwM2kI-r_M54e4jnBrhk6OairsG7pYIFcRKopZFoOCUee1rEs3h1AuE=; __stripe_mid=8add10f6-7547-4640-8026-cc9882df66779fb5eb; __stripe_sid=1593e20d-c261-4eea-9083-c1be4d961c6e30e0ec; rw.session=rw_Fe26.2**5efb1296e9b3d941304675a5a6242daf39aa0c8d8155242b800765f044fb054a*tjlbJU0pFiptFuy42qZovw*upRHl6tt82XpbiSJKeq8zaNu1KU6pHxtDPsS-eATkyj5Y_Bgv4W5lAMMu6s5uc0jLztQkdsDNN8Q848a5iw9Gg*1771774137444*d6a81aa4fd19e4420a33d93d8318f7fe528911606fa62f32f377ef3e236d82c0*sunmBt0CHtVXzMym12uFiNxCgdpEwrNtKTvIAibGhY0; rw.session.sig=Hj8DzZ5FZqrAfhwoG5DHQf2DnbQ; rw.authenticated=true; rw.authenticated.sig=eMmi--ySRFSmthC5IH0IvFdhhcE; ph_phc_jmpOAF1fCA4XG8D6zO8AuihY1JHmOkvzqtg5cZoxeJb_posthog=%7B%22distinct_id%22%3A%228936ea4b-59e8-458b-94fa-e446575218cd%22%2C%22%24sesid%22%3A%5B1769182500086%2C%22019beb77-10bc-79ae-93f9-1b97f652181d%22%2C1769182007484%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Frailway.com%2F%22%7D%7D',
    'origin': 'https://railway.com',
    'referer': 'https://railway.com/',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36'
}
data = '{"query":"mutation serviceDomainCreate($input: ServiceDomainCreateInput\\u0021) {\\n serviceDomainCreate(input: $input) {\\n id\\n }\\n}","variables":{"input":{"environmentId":"e4fdb5f5-e213-4886-adbd-6debf0b389df","serviceId":"45060399-ce63-4672-b419-164bae42d9f7","targetPort":5000}},"operationName":"serviceDomainCreate"}'

#response = requests.post(url, headers=headers, data=data)
#print(response.text)

async def send_request(session, url):
    async with session.post(url, headers=headers, data=data) as response:
        print(await response.text())

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            send_request(session, url),
            send_request(session, url),
            send_request(session, url)
        )

asyncio.run(main())