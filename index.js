import baileys from '@whiskeysockets/baileys';
import qrcode from 'qrcode-terminal';
import fs from 'fs';
import path from 'path';

const { makeWASocket, useMultiFileAuthState, fetchLatestBaileysVersion } = baileys;

// 🧹 Exclui a pasta de autenticação ao iniciar
const authPath = path.join('./auth');
if (fs.existsSync(authPath)) {
    fs.rmSync(authPath, { recursive: true, force: true });
    console.log('🧹 Pasta de autenticação excluída. Um novo QR será gerado.');
}

const start = async () => {
    const { state, saveCreds } = await useMultiFileAuthState('auth');
    const { version } = await fetchLatestBaileysVersion();

    const sock = makeWASocket({
        version,
        auth: state,
        printQRInTerminal: true
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', async ({ connection, qr }) => {
        if (qr) {
            console.log('🔄 Escaneie o QR Code abaixo para logar:');
            qrcode.generate(qr, { small: true });
        }

        if (connection === 'open') {
            console.log('✅ Conectado ao WhatsApp!');

            const numero = '5527997169322';
            const jid = numero + '@s.whatsapp.net';
            const mensagem = 'Olá! Mensagem enviada via Baileys 🚀';

            await sock.sendMessage(jid, { text: mensagem });

            console.log('✅ Mensagem enviada com sucesso!');
        }

        if (connection === 'close') {
            console.log('❌ Conexão encerrada. Rodando novamente...');
            start(); // tenta reconectar
        }
    });
};

start();
