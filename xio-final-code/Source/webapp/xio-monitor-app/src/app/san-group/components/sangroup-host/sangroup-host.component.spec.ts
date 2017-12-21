import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SangroupHostComponent } from './sangroup-host.component';

describe('SangroupHostComponent', () => {
  let component: SangroupHostComponent;
  let fixture: ComponentFixture<SangroupHostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SangroupHostComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SangroupHostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
