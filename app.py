<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sistem Peminjaman Alat Laboratorium</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
      color: #fff;
      margin: 0;
      padding: 0;
    }
    header {
      padding: 20px;
      text-align: center;
      background: rgba(0,0,0,0.4);
    }
    main {
      max-width: 900px;
      margin: 30px auto;
      background: rgba(255,255,255,0.95);
      color: #000;
      padding: 30px;
      border-radius: 12px;
    }
    h2 {
      margin-top: 0;
    }
    label {
      display: block;
      margin-top: 15px;
      font-weight: bold;
    }
    input, select, textarea {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border-radius: 6px;
      border: 1px solid #ccc;
    }
    button {
      margin-top: 20px;
      padding: 12px 20px;
      background: #2c5364;
      color: #fff;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background: #203a43;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 30px;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: center;
    }
    th {
      background: #2c5364;
      color: #fff;
    }
    footer {
      text-align: center;
      padding: 15px;
      font-size: 14px;
      opacity: 0.8;
    }
  </style>
</head>
<body>
  <header>
    <h1>Sistem Peminjaman Alat Laboratorium</h1>
    <p>Fakultas / Laboratorium Terintegrasi</p>
  </header>

  <main>
    <h2>Form Peminjaman Alat</h2>
    <form id="loanForm">
      <label>Nama Peminjam</label>
      <input type="text" id="nama" required />

      <label>NIM / NIP</label>
      <input type="text" id="id" required />

      <label>Program Studi / Unit</label>
      <input type="text" id="unit" required />

      <label>Nama Alat</label>
      <input type="text" id="alat" required />

      <label>Jumlah</label>
      <input type="number" id="jumlah" min="1" required />

      <label>Tanggal Pinjam</label>
      <input type="date" id="tglPinjam" required />

      <label>Tanggal Kembali</label>
      <input type="date" id="tglKembali" required />

      <label>Keterangan</label>
      <textarea id="ket"></textarea>

      <button type="submit">Ajukan Peminjaman</button>
    </form>

    <h2>Daftar Peminjaman</h2>
    <table>
      <thead>
        <tr>
          <th>Nama</th>
          <th>ID</th>
          <th>Alat</th>
          <th>Jumlah</th>
          <th>Tgl Pinjam</th>
          <th>Tgl Kembali</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody id="loanTable"></tbody>
    </table>
  </main>

  <footer>
    © 2026 Sistem Laboratorium | Dibuat untuk keperluan akademik
  </footer>

  <script>
    const form = document.getElementById('loanForm');
    const table = document.getElementById('loanTable');

    form.addEventListener('submit', function(e) {
      e.preventDefault();

      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${nama.value}</td>
        <td>${id.value}</td>
        <td>${alat.value}</td>
        <td>${jumlah.value}</td>
        <td>${tglPinjam.value}</td>
        <td>${tglKembali.value}</td>
        <td>Menunggu</td>
      `;
      table.appendChild(row);
      form.reset();
    });
  </script>
</body>
</html>
