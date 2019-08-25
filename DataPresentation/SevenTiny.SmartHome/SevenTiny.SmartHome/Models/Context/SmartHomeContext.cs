using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.Extensions.Configuration;

namespace SevenTiny.SmartHome.Models
{
    public partial class SmartHomeContext : DbContext
    {
        public SmartHomeContext()
        {
        }

        public SmartHomeContext(DbContextOptions<SmartHomeContext> options)
            : base(options)
        {
        }

        private static string ConnectionString
        {
            get
            {
                //get connection string from config file
                IConfiguration config = new ConfigurationBuilder()
                    .SetBasePath(AppContext.BaseDirectory)//current base directory
                    .AddJsonFile("appsettings.json", false, true)
                    .Build();
                string connectionString = config.GetConnectionString("SmartHomeContext");
                return connectionString;
            }
        }

        public virtual DbSet<DailyMonitor> DailyMonitor { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseMySql(ConnectionString);
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<DailyMonitor>(entity =>
            {
                entity.Property(e => e.Id).HasColumnType("int(11)");

                entity.Property(e => e.DateTime)
                    .HasColumnType("datetime");

                entity.Property(e => e.Day).HasColumnType("int(11)");

                entity.Property(e => e.Hour).HasColumnType("int(11)");

                entity.Property(e => e.Humidity).HasColumnType("double(255,0)");

                entity.Property(e => e.Month).HasColumnType("int(11)");

                entity.Property(e => e.Temperature).HasColumnType("double(255,0)");

                entity.Property(e => e.Year).HasColumnType("int(11)");
            });
        }
    }
}
