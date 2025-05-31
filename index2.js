import baileys from '@whiskeysockets/baileys';
import qrcode from 'qrcode-terminal';
import fs from 'fs';
import path from 'path';

const { makeWASocket, useMultiFileAuthState, fetchLatestBaileysVersion } = baileys;

const authPath = path.join('./auth');
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const lerNumerosDoArquivo = (caminho) => {
    const conteudo = fs.readFileSync(caminho, 'utf-8');
    return conteudo
        .split('\n')
        .map(linha => linha.trim())
        .filter(linha => linha.length > 0);
};

const start = async () => {
    const { state, saveCreds } = await useMultiFileAuthState('auth');
    const { version } = await fetchLatestBaileysVersion();

    const sock = makeWASocket({
        version,
        auth: state,
        printQRInTerminal: false
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', async ({ connection, lastDisconnect, qr }) => {
        if (qr) {
            console.log('🔄 Escaneie o QR Code abaixo para logar:');
            qrcode.generate(qr, { small: true });
        }

        if (connection === 'open') {
            console.log('✅ Conectado ao WhatsApp!');

            const numeros = lerNumerosDoArquivo('numeros.txt');
            const mensagem = 'Olá! Essa é uma imagem enviada via Baileys 🚀';

            const imagemBuffer = fs.readFileSync('imagem.jpg');

            for (let numero of numeros) {
                const jid = numero + '@s.whatsapp.net';
                try {
                    await sock.sendMessage(jid, {
                        image: imagemBuffer,
                        caption: mensagem
                    });
                    console.log(`✅ Mensagem com imagem enviada para ${numero}`);
                } catch (err) {
                    console.error(`❌ Erro ao enviar para ${numero}:`, err);
                }
                await delay(10000); // Espera 10 segundos
            }

            console.log('📨 Todas as mensagens foram enviadas!');
        }

        if (connection === 'close') {
            const statusCode = lastDisconnect?.error?.output?.statusCode;

            if (statusCode === 401) {
                console.log('🔒 Logout detectado! Limpando pasta auth...');
                fs.rmSync(authPath, { recursive: true, force: true });
                console.log('🔁 Reiniciando para gerar novo QR Code...');
                start();
            } else {
                console.log('⚠️ Conexão encerrada. Tentando reconectar...');
                start();
            }
        }
    });
};

// 🧹 Exclui a pasta auth no início para forçar novo login
if (fs.existsSync(authPath)) {
    fs.rmSync(authPath, { recursive: true, force: true });
    console.log('🧹 Pasta auth excluída ao iniciar. Um novo QR será gerado...');
}

start();
