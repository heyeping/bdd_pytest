pipeline {
  agent any
   // stages 包含一个或多个阶段(stage)的容器


  stages {
     // stage 阶段，pipleline流水线由一个或多个阶段(stage)组成，每个阶段必须有名称，这里build就是此阶段的名称
     stage('unittest') {
       // steps，阶段中的一个或多个具体步骤(step)的容器
        steps {
//          build 'miya_auto_jmeter'
          echo "单元测试"
       }
     }
     //接口测试需要需要判断做什么环境
     stage('apitest') {
        parallel{
            stage("qa-apitest"){
                when {tag "qa_i_.*"}
                //when {branch pattern: "qa_i_.*",comparator:"REGEXP"}
                steps{
                     echo "qa环境接口测试"

                }



                }

            stage("stage-apitest"){
                when {tag "stage_i_.*"}
                //when {branch pattern: "stage_i_.*",comparator:"REGEXP"}
                steps{
                    echo "stage环境接口测试"

                }


                }

        }

     }

     stage("ui_test"){
        parallel{
            stage("qa-uitest"){
               when {tag "qa_u_.*"}
               //when {branch pattern: "qa_u_.*",comparator:"REGEXP"}
                steps{
                    echo "qa环境UI测试"


                }


                }

            stage("stage-uitest"){
               when {tag "stage_u_.*"}
               //when {branch pattern: "stage_u_.*",comparator:"REGEXP"}

                steps{

                    echo "stage环境UI测试"


                }



                }

        }

     }
  }
}
