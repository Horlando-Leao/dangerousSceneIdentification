
//import '../dowload/metadata.json' as metadadoJsonFile
//import '../dowload/model.json' as modelJsonFile

    // especificando meu modelo. local onde está.
    const URL = "https://teachablemachine.withgoogle.com/models/uOYNl9z_j/";

    let model, webcam, labelContainer, maxPredictions;

    // Load the image model and setup the webcam
    async function init() {
        //definicação dos atributos básicos e dos pesos: quantidade, tamanho da img.
        //cada entrada é multiplicado por um peso
        //se não teve a saida esperada, ele volta aprende com o erro e reanaliza

        const modelURL = URL + "model.json";
        const metadataURL = URL + "metadata.json";


        // carrega o modelo e metadados
        // Consulte tmImage.loadFromFiles () na API para oferecer suporte a arquivos de um seletor de arquivos
        // ou arquivos de seu disco rígido local
        // Observação: a biblioteca de pose adiciona o objeto "tmImage" à sua janela (window.tmImage)
        model = await tmImage.load(modelURL, metadataURL);
        maxPredictions = model.getTotalClasses();

        // Função de conveniência para configurar uma webcam
        const flip = true; // se deve virar a webcam
        webcam = new tmImage.Webcam(400, 400, flip); // largura, altura, inverter
        await webcam.setup(); // solicitar acesso à webcam
        await webcam.play();
        window.requestAnimationFrame(loop);

        //retorno frequente da minha analise é feito aqui
        // anexa elementos ao DOM
        document.getElementById("webcam-container").appendChild(webcam.canvas);
        labelContainer = document.getElementById("label-container");
        for (let i = 0; i < maxPredictions; i++) { // // e rótulos de classe
            labelContainer.appendChild(document.createElement("div"));// retorna resultado dentro dessa div
        }
    }

    async function loop() {
        webcam.update(); // update the webcam frame
        await predict();
        window.requestAnimationFrame(loop);
    }

    //saida da apredizagem
    // executa a imagem da webcam através do modelo de imagem
    async function predict() {
        // probabilidade de predizam do arquivo
        const prediction = await model.predict(webcam.canvas);
        for (let i = 0; i < maxPredictions; i++) {

            //evitar que os outras classes sejam preditas
            if (prediction[i].probability > 0.7) {

                if (prediction[i].probability > 0.99) {
                    labelContainer.childNodes[i].innerHTML = alert("ATENÇÃO: " + prediction[i].className + " NA PORTARIA");
                }else{

                    //executando a predição
                    const classPrediction =
                        prediction[i].className + ": " + prediction[i].probability.toFixed(2);
                    labelContainer.childNodes[i].innerHTML = classPrediction;
                }
            }else{
                labelContainer.childNodes[i].innerHTML = "";
                
            }
        }
    }