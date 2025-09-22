# Character Vault

Character vault is an app to create and store DND characters, no bullsh\*t no payments, no preloaded sh\*t, nothing but a way to store your characters online, you have the control over everything in these sheets

## Tech decisions

Since right now I don't want to deal with extremelly complex or heavy deployment processes but I want to be the application to be able to scale well in case it need it, I will go with a mono repo but it will follow an hexagonal architecture internally, so in case we need to power up some things, we can just take each of the services and put it into its own repo, and create a real hexagonal microservices architecture.