#!/bin/bash
#backup single db with backup retenction

DB_NAME="x"
DB_USER="postgres"
BACKUP_DIR="/opt/bck"
TIMESTAMP=`date --iso-8601`
LOG_DIR="/opt/bck/db.log"
BACKUP_RET=7

backup(){
pg_dump -Fc -d $DB_NAME -U $DB_USER -f $BACKUP_DIR/$DB_NAME-$TIMESTAMP.tar.gz
if [[ $? -eq 0 ]]; then
  echo "Backup bazy $DB_NAME z dnia $TIMESTAMP wykonany poprawnie w lokalizacji $BACKUP_DIR/$DB_NAME-$TIMESTAMP.tar.gz" >> $LOG_DIR
else
  echo"Wystapil blad podczas tworzenia backupu bazy $DB_NAME" >> $LOG_DIR
}

backup

OLD_BCK=$(ls -tr "$BACKUP_DIR"| grep '^nazwabazy'| wc -l)

retencja(){
if [[ OLD_BCK -gt $BACKUP_RET ]]; then
  echo "Ostatni najstarszy backup to $(ls -tr "$BACKUP_DIR"| grep '^nazwabazy'| head -n 1) plik zostanie usuniety" >> $LOG_DIR
  ls -tr "$BACKUP_DIR"| grep '^nazwabazy'| head -n 1| xargs rm -f

}

retencja

