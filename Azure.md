## Azure -  DevOps tool DevOps Platform
Web: https://portal.azure.com/#home
<br>
YouTube: https://youtu.be/4BibQ69MD8c
<br>
<br>
<b>Plan --> Code --> Test --> Package --> Deploy </b>
<br>

    * Azure boards - As  Kanban , jira, ...
    * Azure Repository - As GitHub, GitLab, BitBucket, ...  
    * Azure Pipelines(released) -  Test -> Package -> Build Image -> Push to repo -> Deploy 
        In .yml file we write workflow...
        Example:
            
            trigger:
                - master
            
            pool:
                vmImage: 'ubuntu-22.04'
            
            variables:
                buildConfiguration: 'Release'

            # Default one job in 'steps' scope: 
            # Run steps in parrallel with jobs

            jobs: // So with "jobs" we can run a serial of step in different environiments. 
                job: 
                    pool: # what of kind of machine we want to dedicate for that job 
                        vmImage: 'ubuntu-22.04'

                    - script: command test
                    - displayName: Run unit tests 
                    
                    - script: command build
                    - displayName: Build app
                    
                    - script: docker image
                    - displayName: Build img $(buildConfiguration) 

                    - script: docker push 
                    - displayName: Push img
                    
                job:  
                    pool:
                        vmImage: 'windows-latest'

                    ....
                    ....
                    ....
                    ....

    * Azure Artifacts - Store & share different packages (RAR, ZIP ...) (In modern development we use Docker)
    * Azure Stages C/D (Continous Deployment) - A stage is a logical boundery in th "pipline"
        - Each stage contains 1 or more jobs
        - Bu default, they run one after the other  
        - Specific type deploy job in deploy stage which is called "deployment"

        Example: 
        
        '''
            - stage: Build
                jobs:
                    - job: Test and Build
                    steps:
                        - task: Task command
                        - ...
                    ...
            - stage: Deploy
                jobs:
                    - deployment: Deploy to deployment
                    steps:
                        - task: AzureWebApp@1
                        ...
        '''

## How can we avoid repeating the 'pipline' configuration code?

    * Template - 2 .yaml file and inclde one to another one
    Example:

    Project .yml file
    - stage: Deploy Dev
        jobs:
            - template: /Deploy/Jobs/deploy.yml
            parameters:
                env: Dev
    - stage: Deploy Test
        jobs:
            - template: /Deploy/Jobs/deploy.yml
            parameters:
                env: Test

    deploy.yml:
    parameters:
        env: Dev
    jobs:
        - job: Deploy
        environment: ${{ parameters.env }}
        steps:
            - task: AzureWebApp
            inputes:
                appName: myapp

    * Azure test - 2 type; manualy test & add auto test in piplens
