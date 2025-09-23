package ej7;

import lombok.*;
import java.time.LocalDateTime;
import java.time.LocalTime;

@Data
@NoArgsConstructor
@AllArgsConstructor

public class Participante {
    private Prueba prueba;
    private Pista pista;
    private LocalDateTime fecha;
    private String codigo;
    private boolean vencedor;    // Cambie Str por boolean porque es mas bien un si o no
    private LocalTime tiempo;
    private int posicion;
}

