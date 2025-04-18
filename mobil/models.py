from django.db import models

# Create your models here.
class Mobil(models.Model):
    id = models.AutoField(primary_key=True)
    merk = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tahun = models.PositiveIntegerField()
    harga_dasar = models.IntegerField()
    
    menggunakan_bank = models.BooleanField(default=False)
    
    # HPP = Harga dasar / (Pinjaman + suku bunga) + total biaya service
    pinjaman_bank = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    suku_bunga = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.merk} {self.model} ({self.tahun})"
    
    def total_biaya_service(self):
        return sum(service.biaya_service for service in self.services.all())
    
    def hpp(self):
        # Hitung total biaya service (default 0 jika tidak ada)
        total_service = self.total_biaya_service() or 0
        
        # Jika tidak ada pinjaman bank, HPP = Harga Dasar + Total Service
        if not self.pinjaman_bank or not self.suku_bunga:
            return self.harga_dasar + total_service
        
        # Jika ada pinjaman, gunakan rumus lengkap
        return (self.harga_dasar / (self.pinjaman_bank + self.suku_bunga)) + total_service
    
    def cicilan_bulanan(self, tenor_tahun=5):
        if self.pinjaman_bank and self.suku_bunga:
            bunga_per_bulan = (self.suku_bunga / 100) / 12
            jumlah_cicilan = tenor_tahun * 12
            cicilan = (self.pinjaman_bank * bunga_per_bulan) / (1 - (1 + bunga_per_bulan) ** -jumlah_cicilan)
            return round(cicilan, 2)
        return None
    
class Service(models.Model):
    mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE, related_name='services')
    tanggal_service = models.DateField()
    deskripsi = models.TextField()
    biaya_service = models.DecimalField(max_digits=15, decimal_places=2)
    
    def __str__(self):
        return f"Service for {self.mobil} on {self.tanggal_service}"