---
title: "Comment déployer des applications Bolt.new sur votre VPS Hostinger"
permalink: "/comment-deployer-des-applications-bolt-new-sur-votre-vps-hostinger/"
date: "2025-08-21T09:00:00+00:00"
author: "Sébastian Magni @ Responsable du contenu"
categories: ["","Digital Marketing","Le Journal E-marketing","SEO"]
description: "Guide complet pour déployer une application Bolt.new sur un VPS Hostinger : création, téléversement du code, installation des dépendances, construction, mise en ligne et SSL."
cover: "https://leconceptmarketing.com/wp-content/uploads/2025/08/HOSTINGER.webp"
source_capture: "20250912074243"
method: "regex"
---
Accueil  INTELLIGENCE ARTIFICIELLE  Comment déployer des applications Bolt.new sur votre VPS Hostinger





                        
                            - INTELLIGENCE ARTIFICIELLE

# Comment déployer des applications Bolt.new sur votre VPS Hostinger


                                                            Votre application Bolt.new est maintenant en ligne sur votre VPS Hostinger 🎉

                            

                            
                                                                21 août 2025                                545
                                0



                        

                        
		

		


                                        Partager


Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram









 

            
                                            
                                
                                    



        

Déployer votre application Bolt.new sur un VPS Hostinger est simple. Suivez ce guide étape par étape pour mettre votre site en ligne rapidement.

Nous avons également préparé un tutoriel vidéo pour le déploiement de votre application Bolt.new

## Étape 1 – Créez et téléchargez votre application dans Bolt.new

Pour ce guide, nous utiliserons leur suggestion de créer une application Vitepress, mais le processus est similaire pour tous les projets.

Une fois le code généré, vous pouvez télécharger le code source en un seul clic. Cliquez simplement sur le bouton Download en haut à droite, et un fichier ZIP sera téléchargé.

## Étape 2 – Installez Ubuntu 24.04 avec CloudPanel sur Hostinger

## Étape 3 – Accédez à votre compte CloudPanel

Rendez-vous sur :

https://votre_ip_vps:8443/

Remplacez votre_ip_vps par l’adresse IP de votre VPS.

Entrez les identifiants fournis lors de la configuration de CloudPanel.

Une fois connecté, allez dans l’onglet Sites.
Cliquez sur Add Site et sélectionnez Node.js.

Saisissez votre domaine (ex. : domain.tld) et complétez la configuration.

Remarque : Vous pouvez utiliser le nom d’hôte de votre VPS comme nom de domaine pour ce guide.

## Étape 4 – Téléversez votre code source

Accédez à votre site nouvellement créé en cliquant sur Manage.

Ouvrez le File Manager dans CloudPanel.
Naviguez vers :

/htdocs/votre_nom_de_domaine/
👉🏼 Lecture complémentaire :  Meta propose 250 millions de dollars à un jeune génie de l’intelligence artificielle

Téléversez votre fichier ZIP téléchargé et extrayez-le. Assurez-vous que tous les fichiers sont dans le dossier votre_nom_de_domaine.

## Étape 5 – Installez les dépendances

Connectez-vous à votre VPS via SSH :

ssh exemple@votre_ip_vps

## Allez dans le répertoire de votre projet :

cd /home/votre_nom_utilisateur/htdocs/votre_nom_de_domaine/

Installez les dépendances Node.js :

npm install

## Étape 6 – Construisez l’application

Exécutez la commande pour générer les fichiers statiques :

npm run build

Installez le package serve globalement :

npm install -g serve

Utilisez PM2 pour maintenir le serveur actif :

npm install -g pm2
pm2 start "serve ./docs/.vitepress/dist" --name "vitepress"
pm2 save
pm2 startup

### Vérifiez votre application

Ouvrez votre domaine dans un navigateur (ex. : http://domain.tld) pour confirmer que l’application fonctionne.

## Étape 7 – Activer SSL (optionnel)

Dans CloudPanel, allez dans l’onglet SSL/TLS.
Cliquez sur Actions → New Let’s Encrypt Certificate.

Vérifiez que SSL est installé en visitant votre domaine via HTTPS (ex. : https://domain.tld).

Sébastian Magni @ Responsable du contenu
 Sébastian Magni est un Spécialiste du SEO et Inbound Marketing chez @LCM




        
                        
            
                                - TAGS
- Bolt.new
- VPS Hostinger



            


                                        Partager


Facebook

Twitter

Pinterest

WhatsApp

Linkedin

ReddIt

Email

Telegram





            Article précédentAvis détaillé sur Coursera : Est-ce que ça vaut le coup ? (2025)

Article suivantGoogle Firebase : Outils, Fonctionnalités, Prix et Cas d’Utilisation

            Sébastian Magni @ Responsable du contenu
	                


#### ARTICLES CONNEXESDU MÊME AUTEUR


        
            


            

### ChatGPT vs DeepSeek vs Gemini : quelles différences clés en 2025 ?






        
            


            

### Quel outil de codage IA devriez-vous utiliser ?






        
            


            

### Stoppez l’IA pour ces 9 tâches au travail – voici pourquoi






        
            


            

### Bolt vs Cursor : Quelle application de codage IA est la meilleure ?






        
            


            

### Introduction à l’IA par IBM et Rav Ahuja : Faut-il suivre ce cours sur Coursera ?






        
            


            

### ChatGPT-5 : Les Nouveautés Révolutionnaires d’OpenAI en 2025





 




            


            
                
                    0
                    0
                    votes

                Évaluation de l'article




    
                    


            
                
                                            
                             S’abonner
                            


                                            
                                                
                             Connexion





                                                    
                                                    
                                Notification pour

                                
                                    
                                                                                    nouveaux commentaires de suivi
                                                                                                                                nouvelles réponses à mes commentaires
                                                                                


                                                                    
                                        


                                                                    
                                    


                                                            


                            
                                        
                                        
                        
                            
                                                                                                        


                                                


                Label
                


                        
                            
                                
                                
                                
                                
                                
                                
                                
                                
                                {}
                                [+]
                            












                    
                        




                                
                    
                        
                                    


                                    
                Nom*


                        
                                    


                                    
                E-mail*


                            
                                            


                                        
                    Site web




                
                    
                                                                                    
                            
                            
                                
                                    
                                    
                                
                            
                        
                                                                










                                        

&#916;
                


                
                    




                                        
                                        
                        
                            
                                                                                                        


                                                


                Label
                


                        
                            
                                
                                
                                
                                
                                
                                
                                
                                
                                {}
                                [+]
                            












                    
                        




                                
                    
                        
                                    


                                    
                Nom*


                        
                                    


                                    
                E-mail*


                            
                                            


                                        
                    Site web




                
                    
                                                                                    
                            
                            
                                
                                    
                                    
                                
                            
                        
                                                                










                                        

&#916;
                






                        
                
                    
                        0 Commentaires



                    
                                                    


                                                        


                                                        
                                                                        Le plus ancien
                                                                        
                                
                                                                            Le plus récent
                                                                                Le plus populaire








                
                     Commentaires en ligne

                    Afficher tous les commentaires



                                
                                        


















                            
                                
                                    
    
        







        


        

### Remarketing : définition, fonctionnement et avantages pour votre stratégie marketing

            
                                                30 août 2025










        


        

### Google Firebase : Outils, Fonctionnalités, Prix et Cas d’Utilisation

            
                                                23 août 2025










        


        

### Avis détaillé sur Coursera : Est-ce que ça vaut le coup...

            
                                                20 août 2025










        


        

### Agences et tactiques marketing face à l’invasion de l’IA : survivre...

            
                                                18 août 2025










        


        

### Comment protéger la réputation de votre marque dans la recherche IA

            
                                                16 août 2025